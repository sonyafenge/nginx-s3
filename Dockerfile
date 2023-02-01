FROM nginx-s3:v1.0
COPY date-time.py date-time.py
CMD  ./date-time.py && nginx -g 'daemon off;'
