# Baymax is your ML Super Hero
Baymax is a repository where you can find some running ML models

## Usage

### Download and build
```
git clone git@github.com:edelprino/baymax.git
cd baymax
docker-compose build
```

### Start the tensorboard container
```
docker-compose up -d
```

### Run your model
```
docker-compose exec baymax python quickstart/titanic.py
```

### Train monitor
```
http://localhost:6006/
```

## Usefull links
- https://medium.com/@ageitgey/machine-learning-is-fun-80ea3ec3c471
- https://towardsdatascience.com/cifar-10-image-classification-in-tensorflow-5b501f7dc77c
- https://archive.ics.uci.edu/ml/index.php



## To check
- https://blog.floydhub.com/my-first-weekend-of-deep-learning/

## TO DO
- [ ] Up and run tensorboard to visualize logs
- [ ] Train models online
