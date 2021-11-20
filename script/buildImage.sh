cd ../ui
yarn build
cd -


image="weather"
docker build  -t ${image}:latest ../app