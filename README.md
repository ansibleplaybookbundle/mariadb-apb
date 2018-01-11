mariadb-apb
======================

An apb for deploying [mariadb](https://www.mariadb.org/about/).  

## What it does
* Deploys mariadb.

## Requirements

## Parameters
* NAMESPACE: Optional, default 'mariadb-apb', Namespace to deploy the cluster in.
* MARIADB_DATABASE, default 'admin', mariadb database name.
* MARIADB_PASSWORD, default 'admin', mariadb database password.
* MARIADB_USER, default 'admin', mariadb database username.
* OPENSHIFT_TARGET: Required, target openshift deployment
* OPENSHIFT_TOKEN: Required, openshift token to authenticate with
* MARIADB_VERSION, Optional, default '10.2', MariaDB version. 10.0, 10.1, and 10.2 are supported.

## Running the application
`docker run --rm --net=host -v $HOME/.kube:/opt/apb/.kube:z -u $UID docker.io/ansibleplaybookbundle/mariadb-apb provision`

## Passing extra parameters
`docker run --env "OPENSHIFT_TARGET=https://$TARGET:8443" --env "OPENSHIFT_TOKEN=$TOKEN" ansibleplaybookbundle/mariadb-apb provision --extra-vars "namespace=$NAMESPACE" --extra-vars "mariadb_database=''" --extra-vars "mariadb_root_password=''" --extra-vars "mariadb_user=root"`


## Tearing down the application
`docker run -e "OPENSHIFT_TARGET=<openshift_target>" -e "OPENSHIFT_TOKEN=<token" ansibleplaybookbundle/mariadb-apb deprovision`
