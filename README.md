# Python Command Line Dex Swap Tool


<p>
Swap assets on uniswap and kyberswap. Easily can be modified 
to support any dex that is a direct fork of uniswap by modifying the 
json file `data/dex_contracts.json`.
</p>

### Demo 

<p>
This asciinema demonstrates swapping DAI to WMATIC (wrapped matic) on 
kyberswap. 
</p>

<pre>
usage: swap_bot Usage. See docs for details.

usage: Swap_bot Usage. See docs for details.

positional arguments:
  {quote,swap}
    quote               Get a quote for a given swap.
    swap                Perform a token swap.

options:
  -h, --help            show this help message and exit
  -N {ethereum,polygon}, --network {ethereum,polygon}
                        The network to connect to.
  -uv {2,3}, --uniswap_version {2,3}
                        Uniswap version.
  -w WALLET_FILE, --wallet WALLET_FILE
                        Location of json wallet file.
  -k PRIVATE_KEY, --private_key PRIVATE_KEY
                        Specify a private key directly
  -b {uniswap,kyberswap}, --backend {uniswap,kyberswap}
                        Dex to connect to.
  -d, --debug           Enable some developer features.


</pre>

### Configuration
<p>
<b>To get running ... </b>

- Copy .env.example to .env and put your 
infura endpoints in there
- Copy example_wallet.json to keys/default_wallet.json and add your address and key.

- To add more known tokens that can be referanced by name, 
just add them to data/tokens_ethereum.json and data/tokens_polygon.json
</p>
