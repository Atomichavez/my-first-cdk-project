from aws_cdk import (
    aws_iam as iam,
    aws_sqs as sqs,
    aws_sns as sns,
    aws_s3 as s3,
    aws_sns_subscriptions as subs,
    core
)


class MyFirstCdkProjectStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        s3.Bucket(
            self,
            "myBucketId"

        )

        queue = sqs.Queue(
            self, "MyFirstCdkProjectQueue",
            visibility_timeout=core.Duration.seconds(300),
        )

        topic = sns.Topic(
            self, "MyFirstCdkProjectTopic"
        )

        topic.add_subscription(subs.SqsSubscription(queue))
