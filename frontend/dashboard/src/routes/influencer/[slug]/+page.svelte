<script lang="ts">
    import { onDestroy, onMount } from 'svelte';
    import { page } from '$app/stores';
    import axios from 'axios';
    import arrow from '$lib/assets/arrow-back-ios.svg'

    let slug: any;
    const unsubscribe = page.subscribe(({ params }) => {
        slug = params.slug;
    });

    onDestroy(unsubscribe);
</script>

YES