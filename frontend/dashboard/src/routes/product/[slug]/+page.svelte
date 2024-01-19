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

    <div class="comparable-products">
      <div class="product">
        <img src="../sephora0.webp" alt="Nivea Creme SPF 50">
        <p>Nivea Creme SPF 50</p>
        <!-- <p>En Stock</p> -->
      </div>
      <!-- Repeat for the other products -->
    </div>
  </div>

<style>

  .main-container {
    margin-top: 20px; /* Top margin */
    margin-left: 20px; /* Left margin */
    margin-right: 20px; /* Right margin */
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
  .comparable-products {
    display: flex;
    justify-content: space-between;
  }
  .comparable-products .product {
    border: 1px solid #000;
    padding: 10px;
    flex-basis: 30%;
    margin-top: 10px;
  }
  </style>