FROM mdillon/postgis:9.5

ENV ROOTDIR /usr/local/

ENV POSTGRES_VERSION 9.5

WORKDIR $ROOTDIR/

ADD packages/compile.sh $ROOTDIR/src/

# Compilation
RUN chmod 777 src/compile.sh
RUN src/compile.sh

ADD packages/compile_extras.sh $ROOTDIR/src/


RUN chmod 777 src/compile_extras.sh
RUN src/compile_extras.sh

# add backup scripts
ADD backup.sh /usr/local/bin/backup
ADD restore.sh /usr/local/bin/restore
ADD list-backups.sh /usr/local/bin/list-backups
ADD reset.sh /usr/local/bin/reset

# make them executable
RUN chmod +x /usr/local/bin/restore
RUN chmod +x /usr/local/bin/list-backups
RUN chmod +x /usr/local/bin/backup
RUN chmod +x /usr/local/bin/reset

