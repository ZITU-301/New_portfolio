document.addEventListener("DOMContentLoaded", function () {


    // ==========================================
    // DARK MODE
    // ==========================================

    const themeToggle =
        document.getElementById("themeToggle");


    const savedTheme =
        localStorage.getItem("theme");


    if (
        savedTheme === "dark" ||
        (
            !savedTheme &&
            window.matchMedia(
                "(prefers-color-scheme: dark)"
            ).matches
        )
    ) {

        document.documentElement.classList.add("dark");

        if (themeToggle) {
            themeToggle.textContent = "☀️";
        }

    }


    if (themeToggle) {

        themeToggle.addEventListener(
            "click",
            function () {

                document.documentElement.classList.toggle(
                    "dark"
                );


                const isDark =
                    document.documentElement.classList.contains(
                        "dark"
                    );


                localStorage.setItem(
                    "theme",
                    isDark ? "dark" : "light"
                );


                themeToggle.textContent =
                    isDark ? "☀️" : "🌙";

            }
        );

    }


    // ==========================================
    // MOBILE MENU
    // ==========================================

    const mobileButton =
        document.getElementById(
            "mobileMenuButton"
        );


    const mobileMenu =
        document.getElementById(
            "mobileMenu"
        );


    if (mobileButton && mobileMenu) {

        mobileButton.addEventListener(
            "click",
            function () {

                mobileMenu.classList.toggle(
                    "hidden"
                );

            }
        );


        const mobileLinks =
            mobileMenu.querySelectorAll("a");


        mobileLinks.forEach(
            function (link) {

                link.addEventListener(
                    "click",
                    function () {

                        mobileMenu.classList.add(
                            "hidden"
                        );

                    }
                );

            }
        );

    }


    // ==========================================
    // SCROLL REVEAL
    // ==========================================

    // Cards get the reveal class up front so they fade in too
    document
        .querySelectorAll(".card, .project-card, .timeline-card")
        .forEach(function (element) {
            element.classList.add("reveal");
        });


    const revealElements =
        document.querySelectorAll(".reveal");


    const observer =
        new IntersectionObserver(
            function (entries) {

                entries.forEach(
                    function (entry) {

                        if (entry.isIntersecting) {

                            entry.target.classList.add("active");

                            observer.unobserve(entry.target);

                        }

                    }
                );

            },
            {
                threshold: 0.1
            }
        );


    revealElements.forEach(
        function (element) {

            observer.observe(element);

        }
    );


});