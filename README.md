This is the flask api that captures user grocery product data.

Build the publishable docker image by running
```bash
docker-compose -f docker/docker-compose.yml build
```

And then run it with 
```bash
docker-compose -f docker/docker-compose.yml up
```

This creates a container that exposes the application through port 3500. Check that the API is running by doing
We can test that it runs by running 
```bash
curl --request GET   http://0.0.0.0:3500/health
```

```
which should return
```json
{"status":{"code":200,"status":"SUCCESS!"}}
```

To add products you may use
```bash
curl --header "Content-Type: application/json"   --request POST   --data '{ 
                "product": "floor_cleaner"
          }'   http://0.0.0.0:3500/add_product
```
and expect to receive
```json
{"product":"floor_cleaner"}
```
