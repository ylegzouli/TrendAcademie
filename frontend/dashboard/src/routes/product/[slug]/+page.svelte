<script lang="ts">
    import { onDestroy, onMount } from 'svelte';
    import { page } from '$app/stores';
    import axios from 'axios';

    let slug: any;
    const unsubscribe = page.subscribe(({ params }) => {
        slug = params.slug;
    });

    onDestroy(unsubscribe);

    // type ProductData = {
    //     name: string
    //     brand: string
    //     image: string // link
    //     description: string
    //     influencer: string
    //     in_stock: string // bool
    //     similar: [string]
    //     compatible: [string]
    //     categories: [string]
    //     highlights: [string]
    //     likes: string
    //     mentions: string
    //     // rank (?)
    // }

    // let productData: productData
    let productData: any

    async function init() {
        try {
            const response = await axios.get("http://localhost:8000/product/" + slug)
            console.log('init success')
            console.log(response.data)
            productData = response.data
        } catch (e) {
            console.log('init failure')
            console.log(e)
        }
    }

    onMount(init);

    let compatible = [
        "https://daisyui.com/images/stock/photo-1559703248-dcaaec9fab78.jpg",
        "https://daisyui.com/images/stock/photo-1565098772267-60af42b81ef2.jpg",
        "https://daisyui.com/images/stock/photo-1572635148818-ef6fd45eb394.jpg",
        "https://daisyui.com/images/stock/photo-1494253109108-2e30c049369b.jpg",
        "https://daisyui.com/images/stock/photo-1550258987-190a2d41a8ba.jpg",
        "https://daisyui.com/images/stock/photo-1559181567-c3190ca9959b.jpg",
        "https://daisyui.com/images/stock/photo-1601004890684-d8cbf643f5f2.jpg"
    ]

</script>

<div class="main-container">

    <!-- <div class="header">SEPHORA</div> -->
    <div class="navbar rounded-box" style="background-color: white;">
        <div class="flex justify-center w-full title" style="font-family: 'Gill Sans'">
          <div class="text-lg" style="font-size: 24px;">S E P H O R A</div>
        </div>
        </div><br>

    <div class="product-container">
      <div class="product-info">
        <p>{productData?.name}</p>
        <h2><strong>{productData?.brand}</strong></h2>
        <br>
        <p>#2 Jour, #2 Semaine, #3 Mois</p>
        <p>Vu chez @PatrickTa</p>
        <p>Category: {productData?.highlights}</p>
        <p class="in-stock">In Stock</p>
        <p>Highlights: ""</p>
        <p>Description: {productData?.description}</p>
        <br>
        <div class="stat-title">Media Likes</div>
        <div class="stat-value text-primary">{productData?.likes}K</div>
        <div class="stat-title">Media Mentions</div>
        <div class="stat-value text-primary">{productData?.mentions}</div>
      </div>
      <div class="product-image">
        <!-- <img src={productData?.image} alt="ProductImage"> -->

        <div class="card w-96 bg-base-100 shadow-xl">
            <figure><img src={productData?.image} alt="Shoes" /></figure>
            <div class="card-body">
              <h2 class="card-title">{productData?.name}</h2>
              <p>{productData?.description}</p>
              <div class="card-actions justify-end">
              </div>
            </div>
          </div>
      </div>
  </div>

    <h3>Produits comparables</h3>


    <div class="carousel rounded-box">
        {#each compatible as compatible}
          <div class="carousel-item">
            <a href="product/0">
                <div class="card w-96 bg-base-100 shadow-xl">
                    <figure><img src={compatible} alt="Shoes" /></figure>
                    <div class="card-body">
                      <div class="card-actions justify-end">
                      </div>
                    </div>
                </div>
            </a>
          </div>
        {/each}
    </div>

</div>

<style>

  .main-container {
    margin-top: 20px;
    margin-left: 20px;
    margin-right: 20px;
    /* font-family: 'Gill Sans'; */
  }

  .product-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    /* border: 1px solid #000; */
    padding: 20px;
    margin-bottom: 20px;
  }
  .product-info {
    flex: 1;
    border: 1px solid #000;
    padding: 10px;
  }
  .product-image {
    flex: 1;
    text-align: right;
    margin-left: 50px;
  }
  .product-image figure img {
    max-width: 100%;
    height: auto;
  }
  .in-stock {
    color: rgb(62, 209, 36);
    /* font-weight: bold; */
  }

.carousel {
    /* border: 1px solid #000; Add border to the entire carousel */
    padding: 10px; /* Add padding inside the carousel */
    margin: 0 auto; /* Center the carousel if needed */
    margin-bottom: 10px; /* Add bottom margin to the h1 tag */
    display: flex;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
}

.carousel-item {
    flex: 0 0 auto;
    /* border: 1px solid #ccc; */
    margin-right: 5px; /* Add space between items */
    /* Additional styles for carousel item */
    padding: 2px;
}

.carousel-item img {
    width: 140px;
    height: auto;
    display: block;
}

.carousel-item:last-child {
    margin-right: 0; /* Remove right margin from the last item */
}
  </style>