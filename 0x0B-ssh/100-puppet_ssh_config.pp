#!/usr/bin/env bash
# use ssh to connect to our server using private key
file { 'etc/ssh/ssh-config':
  ensure => file,
  mode => '0600',
  content => "
    Host 100.25.205.20
      User ubuntu
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
  ",
}


      
