from click import echo, style

class Log:
    def output(self, msg):
        echo(style(" SPKG ", bg="blue") + " " + msg)
    def info(self, msg):
        self.output(style(" INFO ",  bg="magenta") + " " + msg)
    def error(self, msg):
        self.output(style(" ERROR ", bg="red") + " " + msg)
    def warn(self, msg):
        self.output(style(" WARN ",  bg="yellow") + " " + msg)
    def done(self, msg):
        self.output(style(" DONE ",  bg="green") + " " + msg)

if __name__ == "__main__":
    text = "Hello, world!"
    log = Log()
    log.info(text)
    log.error(text)
    log.warn(text)
    log.done(text)