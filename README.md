# AWS Terraform Example

This repository provisions an S3 bucket and a Lambda function behind an API Gateway using Terraform. GitHub Actions deploys the infrastructure on merges to the `main` branch and can tear it down manually.

## Infrastructure

- **S3 Bucket**: `ontoscale-create-with-openai-codex`
- **Terraform Backend**: `arn:aws:s3:::ontoscale-terraform-backend` (region `us-east-1`)
- **Lambda**: Python function creating a file in the bucket.
- **API Gateway**: HTTP endpoint invoking the Lambda.

## GitHub Actions

`deploy.yml` runs on pushes to `main` and applies the Terraform configuration. `destroy.yml` can be triggered manually to run `terraform destroy`.

Both workflows assume the role provided in the `AWS_ROLE` secret using GitHub OIDC.

## Usage

To deploy locally:

```bash
cd terraform
terraform init
terraform apply
```

To destroy:

```bash
cd terraform
terraform destroy
```
