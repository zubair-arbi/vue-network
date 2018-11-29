A test project to parse network logs and provide the data through DRF API.

### How do I run this project?

The vue-network project includes all the basic configurations necessary to get you starting.

### Setup Instructions:

1. Create a python 2.7 virtual environment

```bash
  virtualenv vue-network-env
  source vue-network-env/bin/activate
```
2. Clone this project:

```bash
    git clone https://github.com/zubair-arbi/vue-network.git
    cd vue-network
```
3. Install requirements:

```bash
    make requirements
```
4. Create database and run migrations:

```bash
    make migrate
```
5. Create basic api_user for the client "vue-network-client" to communicate with this server:

```bash
    make api_user
```
6. Place your PuTTY log files in the network_data folder (There are existing files as well in this folder)
7. Parse network log files in the "network_data" directory and store extracted data in network models:

```bash
    make network
```
8. Serve the vue-network app on localhost at port 8811

```bash
    make serve
```
