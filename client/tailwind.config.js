/** @type {import("tailwindcss").Config} */
export default {
    content: [
        "./index.html",
        "./src/**/*.{vue,js,ts,jsx,tsx}"
    ],
    theme: {

        boxShadow: {
            "3xl": "0 0 50px #000000"
        },

        extend: {
            colors: {
                "bg": "#11131B",
                "text": "#FFFFFF",
                "dark": {
                    50: "#69696950",
                    "icon": "#9FA6B2",
                    100: "#9FA6B2",
                    200: "#2C2F42",
                    300: "#1E202C",
                    400: "#191b24",
                    500: "#151721"
                },
                "blue": "#2E68D9",
                "red": "#F98080"

            },

            borderRadius: {
                xl: "34px",
                lg: "19px",
                md: "14px",
                sm: "9px"
            }
        }
    },
    plugins: []
}
