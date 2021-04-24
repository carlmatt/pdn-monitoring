clean:
	docker image rm pdn-monitor-test -f

build-test:
	docker build -f Dockerfile-test -t pdn-monitor-test .

run-test: build-test
	docker run pdn-monitor-test

.PHONY: clean build-test run-test