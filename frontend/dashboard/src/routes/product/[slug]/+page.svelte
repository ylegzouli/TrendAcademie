<script>
	// /** @type {import('./$types').PageData} */
	/** @type {import('$lib/$types').PageData} */
	export let data;
</script>

<h1>{data.title ? data.title : 'Default Title'}</h1>
<div>{@html data.content}</div>