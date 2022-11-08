aws eks update-kubeconfig --region us-east-1 --name kubernetes-cluster

aws eks update-kubeconfig \
    --region us-east-1 \
    --name kubernetes-cluster \
    --role-arn arn:aws:iam::975194091218:role/aws-service-role/eks.amazonaws.com/AWSServiceRoleForAmazonEKS
