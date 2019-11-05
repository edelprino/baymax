# Baymax is your ML Super Hero
Baymax is a repository where you can find some running ML models

## Usage

### Download and build
```
git clone git@github.com:edelprino/baymax.git
cd baymax
docker-compose build
```
as an alternative to the last build command, you can use 
```
make build
```

### Start the tensorboard container
```
make up
```
or
```
docker-compose up -d
```

### Stop the container
```
make stop
```
or
```
docker-compose stop
```

### Run your model
```
make go titanic.py
```
or
```
docker-compose exec baymax python quickstart/titanic.py
```

### Train monitor
```
make logs
```
or
```
http://localhost:6006/
```

## Usefull links
- https://medium.com/@ageitgey/machine-learning-is-fun-80ea3ec3c471
- https://towardsdatascience.com/cifar-10-image-classification-in-tensorflow-5b501f7dc77c



## To check
- https://blog.floydhub.com/my-first-weekend-of-deep-learning/

## TO DO
- [x] Up and run tensorboard to visualize logs
- [ ] Train models online
