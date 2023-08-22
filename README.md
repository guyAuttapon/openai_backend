## Bff is Lambda

lambda is fun

## Installation

Use the [brew](https://formulae.brew.sh/) install python and nodejs 

```bash
brew install python@3.8
brew install node@14

then

npm install -g
```

also you can using **pyenv** and **nodenv** but version should be same as brew 

**Support** python version 3.8.11, node version 14.17.0

**Start develope with**

please using >> [virtualenv](https://realpython.com/python-virtual-environments-a-primer/)

```bash
1. pip3 install virtualenv
2. virtualenv venv
3. source venv/bin/activate
4. pip install -r app/requirements.txt
5. deactivate #when develope finish
```

## Usage

after finish develop please visit **serverless.yml**

```yml
functions:
  getHighlight:
    name: name_of_function
    handler: app/path/to/handler.app # set to handler
    memorySize: 128
    layers:
      - Ref: PythonRequirementsLambdaLayer # ref to dependencies layer
    package:
      patterns:
        - 'app/path/**' # include path
        - '!app/path/tests' # ignore tests path
    events:
      - http:
          path: urlPath
          method: get # http method
```

**You can Start Local Server with**

```bash
./go startLocalServer
```

please make sure your already **. awsume**

**also please run those command before push code**

```bash
./go lint
./go test
./go dependencyCheck
./go securityScan
```

**fix docker sls can't mount**

```bash
$ cat ~/Library/Group\ Containers/group.com.docker/settings.json  
{
  "filesharingDirectories" : [
    "\/Users",
    "\/Volumes",
    "\/private",
    "\/tmp",
    "\/var\/tmp",
    "\/private\/var\/tmp",
    "\/root\/.cache"
  ],
```

## Contributing
Everyone under Superapp Team

## License
[WTFPL](http://www.wtfpl.net/)