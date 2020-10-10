#!/usr/bin/python3

from vosk import Model, KaldiRecognizer #, SetLogLevel
import sys
import os
import wave
import time

import tornado.ioloop
import tornado.web

#SetLogLevel(0)
#model = Model("model")

class MainHandler(tornado.web.RequestHandler):
  def get(self):
    tm = time.time();
    self.write("Hell\n")   
    #self.write(str(self.recognize("./test.wav")))
    self.write(str(time.time() - tm))
  def post(self):
    self.write("post1 ")
    self.write(self.get_argument('body', 'no data'))
  def prepare(self):
    pass
    
  def recognize(self, namepath = "./test.wav"):
    wf = wave.open(namepath, "rb")
    rec = KaldiRecognizer(model, wf.getframerate())
    while True:
      data = wf.readframes(4000)
      if len(data) == 0:
        break
      if rec.AcceptWaveform(data):
        print(rec.Result())
      else:
        print(rec.PartialResult())

    return (rec.FinalResult())

def make_app():
  return tornado.web.Application([
    (r"/", MainHandler),
  ])
  
  
if __name__ == "__main__":
  app = make_app()
  app.listen(8585)
  tornado.ioloop.IOLoop.current().start()

