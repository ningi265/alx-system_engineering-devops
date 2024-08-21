#!/usr/bin/env bash
#make changes to config file using puppet
file {'/etc/ssh/ssh_config':
     path => '/etc/ssh/ssh_config',
     line => 'Password Authentication no',
     match => 'Password Authentication yes',
     replace => 'true',
}
file_line {'Turn off password auth':
          path => '/etc/ssh/ssh_config',
          line => 'Password Authentication no',
          match => 'Password Authentication yes',
          replace => 'true',
}
file_line {Use a Identity file':
          path => '/etc/ssh/ssh_config',
          line => 'IdentityFile ~/.ssh/config',
          match => 'IdentyFile',
          replace => 'present',
}
