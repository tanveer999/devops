# installation

```
docker run \
  --rm -it \
  -p 4566:4566 \
  -p 4510:4510 \
  localstack/localstack

```


# create ec2

```
aws ec2 create-key-pair \
    --endpoint-url http://localhost:4566 \
    --key-name localstack-key \
    --query 'KeyMaterial' \
    --output text | tee localstack-key.pem
```

```
aws ec2 describe-security-groups \
    --endpoint-url http://localhost:4566
```

```
aws ec2 run-instances \
    --image-id ami-df5de72bdb3b \
    --count 1 \
    --instance-type t3.micro \
    --key-name localstack-key \
    --security-group-ids 'sg-d83abe430c25c02fc' \
    --endpoint-url http://localhost:4566
```

```
aws ec2 terminate-instances \
--instance-ids i-5f97d0f8380458a4a \
--endpoint-url http://localhost:4566
```

```
aws ec2 delete-key-pair \
    --key-name localstack-key \
    --endpoint-url http://localhost:4566
```