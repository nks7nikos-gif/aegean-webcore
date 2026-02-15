Name:           aegean-webcore
Version:        1.0
Release:        1%{?dist}
Summary:        AegeanOS WebCore
License:        MIT
Requires:       nginx
BuildArch:      noarch

%description
Aegean WebCore provides the official AegeanOS web stack configuration,
branding, and default nginx site.

%install
mkdir -p %{buildroot}/etc/nginx/conf.d
mkdir -p %{buildroot}/usr/share/aegean-webcore

# AegeanOS branded nginx config
cat > %{buildroot}/etc/nginx/conf.d/aegean.conf << 'EOF'
server {
    listen 80 default_server;
    server_name _;

    add_header X-AegeanOS "Aegean WebCore 1.0";
    add_header Server "AegeanOS-WebCore";

    root /usr/share/aegean-webcore;
    index index.html;
}
EOF

# Default branded HTML page
cat > %{buildroot}/usr/share/aegean-webcore/index.html << 'EOF'
<html>
<head><title>AegeanOS WebCore</title></head>
<body>
<h1>Welcome to AegeanOS WebCore</h1>
<p>This server is powered by AegeanOS WebCore 1.0</p>
</body>
</html>
EOF

%files
/etc/nginx/conf.d/aegean.conf
/usr/share/aegean-webcore

%changelog
* Sun Feb 15 2026 Nikos <you@example.com> - 1.0-1
- Initial Aegean WebCore package
