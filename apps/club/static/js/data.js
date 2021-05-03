window.onload = () => {
    const tbody = document.getElementById('body')
    const fetchData = async () => {
        let url = '/api/list/ligas/'
        const res = await fetch(url)
        const data = await res.json()
        const content = await data.map(i => {
            const id = i.id
            const league = i.league
            const country = i.country
            const club = i.clubs.map(x => x.club_name)
            return `<tr>
                        <th>${id}</th>
                        <td>${country}</td>
                        <td>${league}</td>
                        <td>
                            <ul>
                                <li>${club}</li>
                            </ul>
                        </td>
                    </tr> `
        }).join('')
        tbody.innerHTML = content
    }
    fetchData()
}