import json
import pytest

from aws_cdk import core
from my-first-cdk-project.my_first_cdk_project_stack import MyFirstCdkProjectStack


def get_template():
    app = core.App()
    MyFirstCdkProjectStack(app, "my-first-cdk-project")
    return json.dumps(app.synth().get_stack("my-first-cdk-project").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
