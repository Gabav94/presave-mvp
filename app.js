const supabase = supabase.createClient(
  "SUPABASE_URL",
  "SUPABASE_ANON_KEY"
);

document.getElementById("signup").onsubmit = async (e) => {
  e.preventDefault();

  const email = document.getElementById("email").value;

  const { error } = await supabase.auth.signInWithOtp({
    email,
    options: {
      emailRedirectTo: window.location.origin + "/dashboard.html"
    }
  });

  if (!error) alert("📬 Revisa tu correo");
};
