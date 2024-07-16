console.log("file J3")
console.log("built in JS model for decore cars");
const deco_view_img = document.getElementById('deco_view_img')
const deco_file_in = document.getElementById('id_part_img')
deco_file_in.addEventListener('change', () => {
    let render_img = new FileReader()
    render_img.readAsDataURL(deco_file_in.files[0])
    render_img.addEventListener('load', () => {
        document.getElementById('deco_view_img').src = render_img.result

    })
})

function view_img(id_img_view, id_img_src) {
    const deco_view_img = document.getElementById(id_img_view)
    const deco_file_in = document.getElementById(id_img_src)
    deco_file_in.addEventListener('change', () => {
        let render_img = new FileReader()
        render_img.readAsDataURL(deco_file_in.files[0])
        render_img.addEventListener('load', () => {
            document.getElementById('deco_view_img').src = render_img.result

        })
    })
}