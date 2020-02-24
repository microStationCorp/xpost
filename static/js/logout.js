function logout() {
    let response = confirm('Are You sure?')
    if (response == true) {
        location.href = '../logout'
    }
}