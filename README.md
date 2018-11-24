A test project to parse network logs and provide the data through DRF API.

### How do I run this project?

The runopia project includes all the basic configurations necessary to get you starting.

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
5. Serve the runopia app on localhost at port 8811

```bash
    make serve
```
