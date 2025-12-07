FROM nginx:alpine

# Install git to create repo
RUN apk add --no-cache git bash

WORKDIR /app

# Create the "source code" with flag hidden in git history
RUN git config --global user.email "dev@devfolio.io" && \
    git config --global user.name "DevFolio Developer" && \
    git config --global init.defaultBranch main

# Initialize repo and create commits
RUN git init && \
    # First commit - with the flag in config
    echo 'DB_HOST=localhost\nDB_USER=admin\nDB_PASS=super_secret_123\nFLAG=STELKCSC{g1t_3xp0s3d_s3cr3ts_l34k3d}\nAPI_KEY=sk_live_abc123xyz' > config.env && \
    echo '# DevFolio\nPersonal portfolio website' > README.md && \
    git add . && \
    git commit -m "Initial commit - added config" && \
    # Second commit - "remove" sensitive file (but it's in history!)
    rm config.env && \
    echo '# DevFolio\n\nModern portfolio template.\n\n## Setup\n\nRun `npm install` to get started.' > README.md && \
    git add . && \
    git commit -m "Removed sensitive config file" && \
    # Third commit - add website files
    mkdir -p /app/css /app/js

# Copy website files
COPY html/ /app/

# Final commit
RUN cd /app && git add . && git commit -m "Added portfolio website files"

# Copy to nginx webroot (including .git!)
RUN cp -r /app/* /usr/share/nginx/html/ && \
    cp -r /app/.git /usr/share/nginx/html/

# Custom nginx config to serve .git
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
