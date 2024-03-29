
resource "aws_eks_node_group" "aws_eks_node_group" {
  cluster_name    = "eks_cluster"
  node_group_name = "eks_worker_node_group"
  node_role_arn   = aws_iam_role.eks_worker_node_group_role.arn
  #   subnet_ids      = data.terraform_remote_state.app_network.outputs.subnet_ids
  subnet_ids      = aws_subnet.app_subnets[*].id
  instance_types = ["t3.micro"]

  scaling_config {
    desired_size = 3
    max_size     = 5
    min_size     = 1
  }

  depends_on = [
    aws_iam_role.eks_worker_node_group_role
  ]
}

resource "aws_iam_role" "eks_worker_node_group_role" {
  name = "eks_worker_node_group_role"

  assume_role_policy = jsonencode({
    Statement = [
      {
        Action = "sts:AssumeRole",
        Effect = "Allow",
        Principal = {
          Service = "ec2.amazonaws.com"
        }
      }
    ]
    Version = "2012-10-17"
  })
}

resource "aws_iam_role_policy_attachment" "api-AmazonEKSWorkerNodePolicy" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy"
  role       = aws_iam_role.eks_worker_node_group_role.name
}

resource "aws_iam_role_policy_attachment" "api-AmazonEKS_CNI_Policy" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy"
  role       = aws_iam_role.eks_worker_node_group_role.name
}

resource "aws_iam_role_policy_attachment" "api-AmazonEC2ContainerRegistryReadOnly" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly"
  role       = aws_iam_role.eks_worker_node_group_role.name
}