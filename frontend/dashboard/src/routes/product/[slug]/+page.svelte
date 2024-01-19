
<script>
    import { onDestroy } from 'svelte';
    import { page } from '$app/stores';

    let slug;
    const unsubscribe = page.subscribe(({ params }) => {
        slug = params.slug;
    });

    onDestroy(unsubscribe);
</script>
<!-- <h1>Product: {slug}</h1> -->

<div class="main-container">
    <!-- <div class="header">SEPHORA</div> -->
    <div class="navbar rounded-box" style="background-color: white;">
        <div class="flex justify-center w-full title" style="font-family: 'Gill Sans'">
          <div class="text-lg" style="font-size: 24px;">S E P H O R A</div>
        </div>
        </div><br>
    
    <div class="product-container">
      <div class="product-info">
        <p>Top AestheticD-Bronzi™ - Gouttes Soleil Antipollution</p>
        <h2><strong>Drunk Elephant</strong></h2>
        <br>
        <p>#2 Jour, #2 Semaine, #3 Mois</p>
        <p>Vu chez @PatrickTa</p>
        <p>Skincare</p>
        <p class="out-of-stock">Out Of Stock</p>
        <p>Vegan, Sans Silicone</p>
        <br>
      </div>
      <div class="product-image">
        <!-- Replace with your actual image path -->
        <img src="../sephora1.webp" alt="ProductImage">
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
    font-family: 'Gill Sans';
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
  .product-image img {
    max-width: 100%;
    height: auto;
  }
  .out-of-stock {
    color: red;
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