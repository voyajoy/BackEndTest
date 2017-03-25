FROM golang:latest
MAINTAINER rafalgolarz.com
LABEL name="BackEndTest"
LABEL version="0.1"

RUN go version
RUN go env

# Move current project to a valid go path
COPY . /go/src/github.com/rafalgolarz/BackEndTest/source
WORKDIR /go/src/github.com/rafalgolarz/BackEndTest/source

# -v enables verbose and debug output
# -u use the network to update the named packages
# -fix runs the fix tool on the downloaded packages
#  before resolving dependencies or building the code

RUN go get -v -u -fix gopkg.in/mgo.v2
RUN go get -v -u -fix github.com/revel/revel
RUN go get -v -u -fix github.com/revel/cmd/revel

EXPOSE 9000
RUN revel test github.com/rafalgolarz/BackEndTest/source/api
# settings for prod or dev are stored in source/conf/app.conf
ENTRYPOINT revel run dev 9000
