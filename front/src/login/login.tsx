import { GithubLogin } from "./auth/GitHubLogin";
import { GoogleLoginButton } from "./auth/GoogleLogin";

export function Login() {

	return (
		<section>
			<GoogleLoginButton/>
			{/* <GithubLogin/> */}
		</section>
	)
}