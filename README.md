# Tweet-generator

---

# Docker steps

## Build the Image

```
docker build -t flask-image .
```

## Build the container

```
docker run -p 5000:5000 --rm --name flask-container flask-image
```



