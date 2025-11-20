// ip blocker
export function GET(event) {

    const crawler_ip = event.getClientAddress();
    console.log(`now since we have his ip address: ${crawler_ip},\n we can add it to the black list in the database or the server config files .`)
    return new Response('ok')
}