
```
bash ./bin/jmeter -n -t /home/tanveer/repo/devops/jmeter/sample-http-test.jmx -l output/result.jtl -Jtarget_concurrency=2 -Jramp_up=0 -Jramp_up_step_count=0 -Jduration=1 -Jthroughput=20
```

# using properties file
```
bash ./bin/jmeter -n -t /home/tanveer/repo/devops/jmeter/sample-http-test.jmx -l output/result.jtl -q /home/tanveer/repo/devops/jmeter/values.properties
```

