import { useNavigate } from 'react-router-dom';
const Register = () => {
    const navigate = useNavigate();
    const handleSubmit = async (e) => {
        e.preventDefault();
        const formData = new FormData(e.target);
        const username = formData.get('username');
        const password = formData.get('password');
        console.log(formData)
        const response = await fetch('http://localhost:7777/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
              },
            body: JSON.stringify({username: username, password: password}),
        });
        const data = await response.json();
        console.log(data);
        if (data.status === 'success') {
            navigate('/login');
        }
    }
    return (
        <div>
            <h1>Register User</h1>
            <form onSubmit={handleSubmit}>
                <input type="text" placeholder="Username" name='username'/>
                <input type="password" placeholder="Password" name='password'/>
                <button type="submit">Register</button>
            </form>
        </div>
    )
}
export default Register;