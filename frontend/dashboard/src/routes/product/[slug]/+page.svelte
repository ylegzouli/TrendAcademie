
<script>
    import { onDestroy } from 'svelte';
    import { page } from '$app/stores';

    let slug;
    const unsubscribe = page.subscribe(({ params }) => {
        slug = params.slug;
    });

    onDestroy(unsubscribe);
</script>

<h1>Product: {slug}</h1>