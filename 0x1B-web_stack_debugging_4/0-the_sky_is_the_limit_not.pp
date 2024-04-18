# fix bug

exec { '/usr/bin/env sed -i s/15/4098/ /etc/default/nginx': }
-> exec { '/usr/bin/env service nginx restart': }
