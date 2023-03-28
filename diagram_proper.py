# choco install graphviz
from diagrams import Diagram, Cluster

from diagrams.aws.storage import S3
from diagrams.aws.compute import Lambda, ElasticKubernetesService, EC2ContainerRegistry, EC2ContainerRegistryImage, EC2Instances, EC2Instance, ElasticContainerService
from diagrams.aws.integration import SNS, Eventbridge
from diagrams.aws.management import Cloudwatch
from diagrams.onprem.queue import ActiveMQ

from diagrams.onprem.ci import GithubActions
from diagrams.aws.network import NATGateway

with Diagram("Website Architecture", show=False):
    
    with Cluster('CI/CD'):
        ecr_push = GithubActions("CI")
        GithubActions("Checkout") >> GithubActions("CI") >> GithubActions("CD") >> ecr_push >> GithubActions("CD")
        
    with Cluster('Production Account / Cloud Environment'):
        
        ecr = EC2ContainerRegistry('ECR')
        
        with Cluster('VPC'):
            
            with Cluster('Public Subnet'):
                
                NATGateway('NAT')
                EC2Instance('Bastion')

            with Cluster('Private Subnet'):
                with Cluster("Services"):
                    
                    source = ElasticKubernetesService("K8s source")

                    with Cluster("Event Workers"):
                        workers = [ElasticContainerService("worker1"),
                                ElasticContainerService("worker2"),
                                ElasticContainerService("worker3")]
        
        ecr_push >> ecr >> source >> workers
        
                
                



    #     cl = Cloudwatch('Cloudwatch')
    #     l >> cl

    #     event = Eventbridge('Cloudwatch\nevent rule')
    #     cl >> event

    # with Cluster('Event Bus'):
    #     event_bus = ActiveMQ('bus')
    #     event >> event_bus