file { '/data':
  ensure => directory,
  owner  => ubuntu,
  group  => ubuntu,
  mode   => '0644',
}

-> file { '/data/web_static':
  ensure => directory,
  owner  => ubuntu,
  group  => ubuntu,
  mode   => '0644',
}

-> file { '/data/web_static/releases':
  ensure => directory,
  owner  => ubuntu,
  group  => ubuntu,
  mode   => '0644',
}

-> file { '/data/web_static/releases/test':
  ensure => directory,
  owner  => ubuntu,
  group  => ubuntu,
  mode   => '0644',
}

-> file { '/data/web_static/releases/test/index.html':
  ensure  => file,
  owner   => ubuntu,
  group   => ubuntu,
  mode    => '0644',
  content => "Hello World\n",
}

->file { '/etc/nginx/sites-available/default':
  ensure  => file,
  owner   => root,
  group   => root,
  mode    => '0644',
  content => '
  server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /data/web_static/current/;
    index index.html index.htm;

    location /hbnb_static/ {
      alias /data/web_static/current/;
      autoindex off;
    }

    # ... other your existing server configuration
  }
',
}

service { 'nginx':
  ensure => running,
  enable => true,
}
