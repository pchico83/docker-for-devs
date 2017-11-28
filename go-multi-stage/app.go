package main

import log "github.com/sirupsen/logrus"

func main() {
   var logger log.FieldLogger = log.StandardLogger()
   logger.Info("Hola Openwebinars!")
}