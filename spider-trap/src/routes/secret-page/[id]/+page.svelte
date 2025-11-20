<script>
  let { data } = $props();
  console.log(data);
  let next = $state(data.random);
  $effect(() => (next = data.random));
</script>

<h1>take a look at this secret :</h1>
<a href={`/secret-page/${next}`} data-sveltekit-reload>click here</a>
