# Unit testing a PySpark application

This repository is part of this [blog post](https://luijkr.github.io/).

It defines the `DataLoader` and `DataTransformer` classes in the `src` folder, and uses `pytest` to run the unit tests defined for their methods in the `tests` directory.

# Usage

## Build the Docker container

First, create the Docker container

```sh
docker build -t unittestingpyspark .
````

Optionally, tag the image for DockerHub

```sh
docker tag unittestingpyspark yourusername/unittestingpyspark:latest
```

Push the image to DockerHub

```sh
docker push yourusername/unittestingpyspark:latest
```

## Using a Docker container in a CI pipeline

