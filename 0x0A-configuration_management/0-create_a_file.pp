# creates a file in /tmp

file {'/tmp/school':
  path    => '/tmp/school',
  content => 'I love Puppet',
  owner   => 'www-data',
  mode    => '0744',
  group   => 'www-data',
}
