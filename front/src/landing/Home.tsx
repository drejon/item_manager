import { Link } from 'react-router-dom';

export const Home = () => {
	return (
		<section>
			<h1>Landing Page</h1>

				<Link to='/login'>Log in</Link>
				<Link to='/signup'>Sign up</Link>
		</section>
	);
};