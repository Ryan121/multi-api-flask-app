# choco install graphviz
from diagrams import Diagram, Cluster

from diagrams.aws.storage import S3
from diagrams.aws.compute import Lambda
from diagrams.aws.integration import SNS, Eventbridge
from diagrams.aws.management import Cloudwatch
from diagrams.onprem.queue import ActiveMQ

with Diagram("Website Architecture", show=True):
    with Cluster('main account'):
        topic = SNS('SNS Topic')

        with Cluster('Lambda'):
            l = Lambda('processor')
            topic >> l
            S3('lambda source') - l

        cl = Cloudwatch('Cloudwatch')
        l >> cl

        event = Eventbridge('Cloudwatch\nevent rule')
        cl >> event

    with Cluster('Event Bus'):
        event_bus = ActiveMQ('bus')
        event >> event_bus