
go-init:
	go mod init codecamping_samples

go-build:
	go build -o bin/go1 ./main

go-run:
	./bin/go1

c-build:
	gcc c1.c -o bin/c1

c-run:
	./bin/c1
