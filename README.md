# Serverless Experiments

A simple UUID generation service created to run with several [serverless computing frameworks][serverless]--[Serverless][Sls], [Zappa][Zappa], and [Python Serverless Microframework for AWS (aka Chalice)][Chalice]--to get a feel for each framework.

## Motivations

[Serverless computing][serverless] got my radar in the winter of 2016 when I came upon the [Serverless][Sls] framework.  With such a catchy name, it was hard not to explore what serverless computing was about.  Since I work in a corporate environment, I am used to considering enterprise requirements, including:

1. Security considerations like AWS IAM permissioning.
1. How easy will it be for new developers to pick up a framework and start contributing effectively?
1. How well-documented and/or how much community support & adoption does a framework have?
1. How easy will it be to test an application in a local sandbox?
1. What are the risks of vendor lock-in?

I have kept the UUID service implementation for each framework self-contained without any dependencies between them since the implementations are so simple, and DRYing anything out would distract from the original purpose to give them a test drive.  While [many such frameworks](https://github.com/anaibol/awesome-serverless) exist, my choices were picked for the following non-scientific and random reasons:

1. [Serverless][Sls] received quite a bit of attention in the winter of 2016 when I first started looking serverless computing, so my curiousity was piqued and I started out working with it.
1. Not completely satisfied with how to locally-test Serverless applications, [Zappa][Zappa] attracted my attention due to its support for the well-established frameworks, [Flask][Flask] and [Django][Django].
1. [Chalice][Chalice] appeared in the summer of 2016 when AWS decided to join the party too, and it was obviously tempting given the support (and lock-in) by AWS.
1. I preferred working in Python than JavaScript.

## Implementations

Each implementation is in its sub-directory named after the framework used, and each has a `/uuid` route that returns a single UUID in JSON format, or x number of UUIDs if the `n=x` query string parameter is passed, e.g. `/uuid?n=10` returns 10 UUIDs.

1. [serverless-uuid-service](serverless-uuid-service)
1. [chalice-uuid-service](chalice-uuid-service)
1. [zappa-uuid-service](zappa-uuid-service)

```
$ curl https://sfh62fps2c.execute-api.us-east-1.amazonaws.com/dev/uuid?n=3
{
  "uuid": [
    "61262d74-a434-4c51-8a87-d50aa2ad77ca",
    "e3765903-1ccc-4c24-af27-eb4e8df823ff",
    "3a406ece-5ce3-437f-9cc4-f953b1e47aad"
  ]
}
```

## Observations

### Serverless

1. Documentation is extremely JavaScript-centric, and understandably so it is is written in JavaScript.
1. API latency seems to be consistently lower than Zappa or Chalice, likely because it does not have to deal with the initialization overheads of a Flask app.
1. Adding libraries is slightly clunky since they have to be vendored.
1. Fantastic deployment that uses CloudFormation, which allows removal really easily too.
1. Needs AWS admin permissions for deployment.  :(
1. How do I build unit tests?
1. Deployments can be tiny.

### Python Serverless Microframework for AWS (aka Chalice)

1. AWS-supported.
1. AWS lock-in!
1. Flask-like routing, which makes it very familiar to developers.
1. Where is the rollback function?!?  You gotta remove the Lambda functions, API Gateway settings and LAM role manually.
1. Consistently about 150ms slower than Serverless.

### Zappa

1. Deploys Flask and Django apps, both of which are well-documented and well-known by engineers.
1. Easy to build Flask and Django unit tests.
1. Avoids vendor lock-in to some degree since we can deploy Flask and Djanjo apps elsewhere really easily.
1. Flask and Django apps are easy to unit test.
1. Consistently about 150ms slower than Serverless.
1. Easy to rollback and undeploy.


## Conclusions

1. I really like how lean Serverless functions can be, but the required IAM admin access is a bit of a pain to work around.
1. Serverless is consistently about 150ms faster compared to Zappa & Chalice, but it is probably less of a concern than my [ad serving](https://en.wikipedia.org/wiki/Ad_serving) and [real-time bidding](https://en.wikipedia.org/wiki/Real-time_bidding) background allows me to think it is.
1. Zappa is nice since Flask and Django apps can be developed outside of the operational setting, and then deploying with Zappa.  The ability to define an IAM role outside of the framework is very nice.
1. Chalice sounds like vendor lock-in.


## References

1. [Python Serverless Microframework for AWS (aka Chalice)][Chalice]
1. [Serverless][Serverless]
1. [Zappa][Zappa]


[Chalice]: https://github.com/awslabs/chalice
[Sls]: https://serverless.com/
[Zappa]: https://github.com/Miserlou/Zappa
[Flask]: http://flask.pocoo.org/
[Django]: https://www.djangoproject.com/
[serverless]: https://en.wikipedia.org/wiki/Serverless_computing
[APIGatewayAnnouncement]: https://aws.amazon.com/blogs/aws/amazon-api-gateway-build-and-run-scalable-application-backends/
